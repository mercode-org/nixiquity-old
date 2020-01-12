{ lib
, buildPythonPackage
, fetchFromGitHub
}:

buildPythonPackage rec {
  pname = "python-pam";
  version = "1.8.4";

  src = fetchFromGitHub {
    owner = "FirefighterBlu3";
    repo = pname;
    rev = "v${version}";
    sha256 = "0gp7vzd332j7jwndcnz7kc9j283d6lyv32bndd1nqv9ghzv69sxp";
  };

  meta = {
    description = "Python pam module supporting py3 (and py2)";
    homepage = https://github.com/FirefighterBlu3/python-pam;
    license = lib.licenses.mit;
  };
}
