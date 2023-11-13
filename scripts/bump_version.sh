git pull --no-edit origin ${ github.event.ref }
CURRENT_VERSION=$(awk -F '"' '/^version/{print $2}' "pyproject.toml")
pdm bumpversion --current-version $CURRENT_VERSION patch pyproject.toml src/unit_grader/__init__.py --verbose --no-configured-files
NEW_VERSION=$(awk -F '"' '/^version/{print $2}' "pyproject.toml")

# Check if there are changes before committing
if git diff --exit-code; then
echo "Version is not updated in pyproject.toml."
exit 1 # Exit with non-zero exit code to indicate failure
else
git remote set-url origin https://x-access-token:${{ secrets.SOUYANG_GITHUB_TOKEN }}@github.com/souyang/unit-grader 
# Commit and push the change on pyproject.toml
git add pyproject.toml
git commit -m "[Bot] Updating version from ${CURRENT_VERSION} to ${NEW_VERSION}"
git push
# Create and publish a new release tag
TAG_NAME="v$NEW_VERSION"
if git rev-parse -q --verify "refs/tags/$TAG_NAME" > /dev/null; then
    echo "Tag $TAG_NAME exists. Deleting remotely..."
    git push origin :"$TAG_NAME"
    echo "Tag $TAG_NAME deleted remotely."
else
    echo "Tag $TAG_NAME does not exist."
fi              
git tag -a "$TAG_NAME" -m "Releasing version $NEW_VERSION"
git push origin "$TAG_NAME"
echo "Tag $TAG_NAME is created remotely."  
git tag -l --sort=-version:refname "v*"
fi