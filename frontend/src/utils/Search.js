export default function(hay, needle, inverted, field) {
  if (!hay || !needle) return hay;
  try {
    let regex = new RegExp(needle, "i");
    if (!inverted) return hay.filter(it => regex.test(it[field]));
    else return hay.filter(it => !regex.test(it[field]));
  } catch {
    return [];
  }
}
