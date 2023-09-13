{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python39  # Specify the Python version you want to use
    pkgs.python39Packages.pip
    # Add other Python packages as needed
  ];

  shellHook = ''
    VENV=.venv
    if [ ! -d $VENV ]; then
      python3 -m venv $VENV
      source $VENV/bin/activate
      pip install -e .
    fi
    source $VENV/bin/activate
    '';
}

