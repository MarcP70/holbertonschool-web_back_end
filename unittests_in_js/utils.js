const Utils = {
	calculateNumber: function (type, a, b) {
		const number_1 = Math.round(a)
		const number_2 = Math.round(b)
		if (type == "SUM") {
			return ((number_1 + number_2));
		}
		if (type == "SUBTRACT") {
			return ((number_1 - number_2));
		}
		if (type == "DIVIDE") {
			if (number_2 == 0) {
				return "Error"
			}
			return ((number_1 / number_2));
		}

	}
}

module.exports = Utils;
