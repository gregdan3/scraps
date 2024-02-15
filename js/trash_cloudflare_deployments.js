// We had hundreds of deployments from a hook to Cloudflare making tons of commits, and there was no way to bulk delete deployments in the UI
// A google search suggested using the API, but I wasn't the project owner and didn't have permission to make a key with this scope over the project
// So, this deleted many of the hundreds of deployments
// It hitches on last-of-branch deployments that throw a challenge (enter the branch name), and will stall if the page is currently full of non-latest production deployments

FIND_BUTTON =
  '//span[text()="Preview"]/../../..//button[@data-testid="more-options-menu-trigger"]';

FIND_DELETE = '//span[text()="Delete deployment"]';

FIND_DELETE_CONFIRM = '//span[text()="Delete"]';

function getElementByXpath(path) {
  return document.evaluate(
    path,
    document,
    null,
    XPathResult.FIRST_ORDERED_NODE_TYPE,
    null,
  ).singleNodeValue;
}

function getElementsByXPath(xpath, parent) {
  let results = [];
  let query = document.evaluate(
    xpath,
    parent || document,
    null,
    XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
    null,
  );
  for (let i = 0, length = query.snapshotLength; i < length; ++i) {
    results.push(query.snapshotItem(i));
  }
  return results;
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function cleanup() {
  var first_elem = getElementsByXPath(FIND_BUTTON);

  while (first_elem) {
    first_elem.forEach(async (element) => {
      element.click();

      var delete_elem = getElementByXpath(FIND_DELETE);
      delete_elem.click();

      var confirm_elem = getElementByXpath(FIND_DELETE_CONFIRM);
      confirm_elem.click();
    });
    await sleep(5000);
    first_elem = getElementsByXPath(FIND_BUTTON);
  }
}
