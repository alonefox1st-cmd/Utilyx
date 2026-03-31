"""
FDB/FSR Database Manager
Handles reading, writing, and manipulating .fdb and .fsr files.

.fdb = Container file (like a zip/archive)
.fsr = Data files inside .fdb (JSON-like or key-value format)
"""

import json
import zipfile
import io
from pathlib import Path
from typing import Any, Dict, Optional


class FSRFile:
    """Represents a single .fsr file with its data."""
    
    def __init__(self, name: str, data: Dict[str, Any] = None, is_keyvalue: bool = False):
        """
        Initialize an FSR file.
        
        Args:
            name: Name of the .fsr file (e.g., "main.fsr")
            data: Dictionary containing the data
            is_keyvalue: If True, uses key-value format; otherwise JSON nested
        """
        self.name = name
        self.data = data or {}
        self.is_keyvalue = is_keyvalue
    
    def to_bytes(self) -> bytes:
        """Convert FSR data to bytes for storage."""
        if self.is_keyvalue:
            # Key-value format with special marker
            content = "<ftb.keyvalues>true<ftb.keyvalues>\n"
            for key, value in self.data.items():
                content += f"{key}={json.dumps(value)}\n"
            return content.encode('utf-8')
        else:
            # JSON nested format
            return json.dumps(self.data, indent=2).encode('utf-8')
    
    @staticmethod
    def from_bytes(name: str, data: bytes) -> 'FSRFile':
        """Create FSRFile from bytes."""
        text = data.decode('utf-8')
        
        # Check if it's key-value format
        if text.startswith("<ftb.keyvalues>true<ftb.keyvalues>"):
            is_keyvalue = True
            lines = text.split('\n')[1:]  # Skip the marker line
            parsed_data = {}
            for line in lines:
                if '=' in line:
                    key, value = line.split('=', 1)
                    try:
                        parsed_data[key.strip()] = json.loads(value.strip())
                    except json.JSONDecodeError:
                        parsed_data[key.strip()] = value.strip()
            return FSRFile(name, parsed_data, is_keyvalue=True)
        else:
            # JSON format
            try:
                parsed_data = json.loads(text)
            except json.JSONDecodeError:
                parsed_data = {}
            return FSRFile(name, parsed_data, is_keyvalue=False)


class FDBFile:
    """Represents a .fdb database file (container of .fsr files)."""
    
    def __init__(self, filepath: Optional[str] = None):
        """
        Initialize FDB file.
        
        Args:
            filepath: Path to existing .fdb file, or None to create new
        """
        self.filepath = filepath
        self.fsr_files: Dict[str, FSRFile] = {}
        
        # Always create/ensure main.fsr exists
        if not self.has_fsr("main.fsr"):
            self.fsr_files["main.fsr"] = FSRFile("main.fsr", {}, is_keyvalue=False)
        
        # Load from file if it exists
        if filepath and Path(filepath).exists():
            self.load(filepath)
    
    def load(self, filepath: str) -> None:
        """Load .fdb file from disk."""
        self.filepath = filepath
        self.fsr_files.clear()
        
        with zipfile.ZipFile(filepath, 'r') as zf:
            for filename in zf.namelist():
                if filename.endswith('.fsr'):
                    data = zf.read(filename)
                    self.fsr_files[filename] = FSRFile.from_bytes(filename, data)
        
        # Ensure main.fsr exists
        if "main.fsr" not in self.fsr_files:
            self.fsr_files["main.fsr"] = FSRFile("main.fsr", {}, is_keyvalue=False)
    
    def save(self, filepath: Optional[str] = None) -> None:
        """Save .fdb file to disk."""
        if filepath:
            self.filepath = filepath
        elif not self.filepath:
            raise ValueError("No filepath specified")
        
        with zipfile.ZipFile(self.filepath, 'w', zipfile.ZIP_DEFLATED) as zf:
            for fsr_name, fsr_file in self.fsr_files.items():
                zf.writestr(fsr_name, fsr_file.to_bytes())
    
    def add_fsr(self, name: str, data: Dict[str, Any] = None, is_keyvalue: bool = False) -> None:
        """Add a new .fsr file."""
        if not name.endswith('.fsr'):
            name += '.fsr'
        self.fsr_files[name] = FSRFile(name, data or {}, is_keyvalue=is_keyvalue)
    
    def remove_fsr(self, name: str) -> None:
        """Remove an .fsr file (can't remove main.fsr)."""
        if name == "main.fsr":
            raise ValueError("Cannot remove main.fsr")
        if name in self.fsr_files:
            del self.fsr_files[name]
    
    def get_fsr(self, name: str) -> Optional[FSRFile]:
        """Get an .fsr file by name."""
        return self.fsr_files.get(name)
    
    def has_fsr(self, name: str) -> bool:
        """Check if .fsr file exists."""
        return name in self.fsr_files
    
    def list_fsrs(self) -> list:
        """List all .fsr files in this database."""
        return list(self.fsr_files.keys())
    
    def get_data(self, fsr_name: str) -> Dict[str, Any]:
        """Get the data from an .fsr file."""
        fsr = self.get_fsr(fsr_name)
        return fsr.data if fsr else {}
    
    def set_data(self, fsr_name: str, data: Dict[str, Any]) -> None:
        """Set the data for an .fsr file."""
        fsr = self.get_fsr(fsr_name)
        if fsr:
            fsr.data = data
    
    def get_all_data_flat(self) -> Dict[str, Dict[str, Any]]:
        """Get all data from all .fsr files as a flat dictionary."""
        return {name: fsr.data for name, fsr in self.fsr_files.items()}


# Convenience functions for quick access
def create_fdb(filepath: str) -> FDBFile:
    """Create a new .fdb file."""
    fdb = FDBFile()
    fdb.filepath = filepath
    fdb.save(filepath)
    return fdb


def open_fdb(filepath: str) -> FDBFile:
    """Open an existing .fdb file."""
    return FDBFile(filepath)
