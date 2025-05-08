{
  buildPythonPackage,
  numba,
  numpy,
  pyserial,
  setuptools,
  wheel,
}:
buildPythonPackage {
  pname = "tinyturing";
  version = "0.1.0";
  pyproject = true;
  src = ./.;

  nativeBuildInputs = [
    setuptools
    wheel
  ];

  propagatedBuildInputs = [
    numba
    numpy
    pyserial
  ];

  pythonImportsCheck = [ "tinyturing" ];
}
