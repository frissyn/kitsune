echo "Removing PKG files/folders..."

rm -r "build"; rm -r "dist"
rm -r "kitsune.py.egg-info"


echo "Removing generated files/folders..."

rm -r "kitsune/__pychache__"
rm "poetry.lock"; rm "pyproject.toml"

echo "Done!"
