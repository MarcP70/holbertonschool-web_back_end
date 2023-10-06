const cleanSet = (set, startString) => {
  if (startString === '') {
    return '';
  }

  const cleanedValues = [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => value.substring(startString.length));

  return cleanedValues.join('-');
};

export default cleanSet;
