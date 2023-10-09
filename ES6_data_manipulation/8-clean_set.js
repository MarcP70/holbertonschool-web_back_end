export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString.length === 0) {
    return '';
  }
  const newSet = new Set();
  set.forEach((value) => {
    if (value && value.startsWith(startString)) {
      newSet.add(value.slice(startString.length));
    }
  });
  return Array.from(newSet).join('-');
}
