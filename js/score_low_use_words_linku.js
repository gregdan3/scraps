/* Must be copied into old.linku.la, expects data to be the word data from jasima */

var ignores = ["core", "widespread", "common"];

for (var word in data) {
  if (ignores.includes(data[word].usage_category)) {
    continue;
  }

  let recognition = data[word].recognition;
  let strings = "";

  let over_threshold = 0;
  for (var date in recognition) {
    // if (date === "2020-04" || date === "2021-10") {
    //   continue;
    // }
    let parsed = parseInt(recognition[date]);
    if (parsed > 22) {
      over_threshold += 1;
    }
    if (parsed < 20) {
      over_threshold -= 1;
    }

    strings += `\n  - ${date}: ${recognition[date]}; `;
  }
  if (over_threshold >= 2) {
    console.log(`${word}: ${strings}`);
    // console.log(word)
  }
}
