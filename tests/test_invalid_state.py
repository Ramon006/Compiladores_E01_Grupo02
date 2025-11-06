import unittest, subprocess, sys, pathlib, json

class InvalidStateTest(unittest.TestCase):
    def test_invalid_state_transition(self):
        rules = "start_state: Inicio\nintents: ok\nstate Inicio:\n  on ok -> NaoExiste\n"
        path = pathlib.Path("temp.cf")
        path.write_text(rules, encoding="utf-8")
        proc = subprocess.run([sys.executable, "tools/chatflow_to_json.py", "temp.cf", "temp.json"], capture_output=True, text=True)
        self.assertNotEqual(proc.returncode, 0)
        path.unlink(missing_ok=True)

if __name__ == "__main__":
    unittest.main()
