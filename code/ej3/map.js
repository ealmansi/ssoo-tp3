function() {
	var text = this.text;
	var find = "<br />";
	var regex = new RegExp(find, "g");
	text = text.replace(regex, "");	//remove <br />
	value = { 
		count: 1, 
		len: text.length 
	};
	var parts = this.helpfulness.split("/");
	parts[0] = parseFloat(parts[0]);
	parts[1] = parseFloat(parts[1]);
	if (parts[1] != 0 && parts[0] <= parts[1])
		emit((parts[0] / parts[1]).toFixed(4),value);	//key as number
}
