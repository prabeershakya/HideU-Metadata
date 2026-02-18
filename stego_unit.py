import unittest
import os
import shutil
import hashlib
import numpy as np
from PIL import Image
from unittest.mock import MagicMock, patch
from stego import ModernForensicsTool 

class TestHideU_Headless(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create a temporary environment and dummy files."""
        cls.test_dir = "test_env_headless"
        os.makedirs(cls.test_dir, exist_ok=True)
        
        # Create a red dummy image (100x100 pixels)
        cls.img_path = os.path.join(cls.test_dir, "test.png")
        Image.new('RGB', (100, 100), color='red').save(cls.img_path)
        
        # Create a dummy text file for hashing
        cls.txt_path = os.path.join(cls.test_dir, "data.txt")
        cls.file_content = b"ForensicData2026\n"  # Store content to verify later
        with open(cls.txt_path, "wb") as f:
            f.write(cls.file_content)

    @classmethod
    def tearDownClass(cls):
        """Cleanup temporary files."""
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    @patch('stego.tk') 
    def setUp(self, mock_tk):
        """Initialize the app with a Mocked GUI."""
        self.mock_root = MagicMock()
        
        # FIX: Force .after() to execute callbacks immediately
        def execute_immediately(delay, callback):
            callback()
        self.mock_root.after.side_effect = execute_immediately

        self.app = ModernForensicsTool(self.mock_root)
        
        # Override the GUI variables with simple Mocks
        self.app.selected_file = MagicMock()
        self.app.secret_message = MagicMock()
        
        # Prevent the UI from updating status/progress
        self.app.update_status = MagicMock()
        self.app.show_progress = MagicMock()

    def test_hashing_logic(self):
        """Test if the MD5 calculation is mathematically correct."""
        # 1. Ask the App to compute the hash
        hashes = self.app.compute_hashes(self.txt_path)
        
        # 2. Compute the "Truth" hash manually using standard library
        truth_md5 = hashlib.md5(self.file_content).hexdigest()
        
        # 3. Compare them
        self.assertEqual(hashes['MD5'], truth_md5)
        print(f"[PASS] Hashing Verified: App({hashes['MD5']}) == Truth({truth_md5})")

    @patch('stego.filedialog.asksaveasfilename') 
    def test_steganography_logic(self, mock_save_dialog):
        """Test the LSB encoding and decoding logic flow."""
        # 1. Setup Input
        secret = "Classified_Info"
        self.app.selected_file.get.return_value = self.img_path
        self.app.secret_message.get.return_value = secret
        
        # 2. Mock the "Save" location
        save_path = os.path.join(self.test_dir, "stego_output.png")
        mock_save_dialog.return_value = save_path
        
        # 3. RUN ENCODE
        self.app._encode_thread()
        self.assertTrue(os.path.exists(save_path))
        
        # 4. RUN DECODE
        self.app.selected_file.get.return_value = save_path
        self.app.stego_display_message = MagicMock()
        
        self.app._decode_thread()
        
        self.app.stego_display_message.assert_called_with(secret)
        print(f"[PASS] Steganography Cycle Verified: '{secret}' preserved.")

    def test_metadata_extraction(self):
        """Test if image properties are correctly read."""
        meta = self.app.extract_image_metadata(self.img_path)
        
        self.assertEqual(meta['Image Properties']['Width'], 100)
        self.assertEqual(meta['Image Properties']['Height'], 100)
        print("[PASS] Metadata Extraction Verified")

if __name__ == '__main__':
    unittest.main()
