function (key, values) {
	reducedValue = { 
		count: 0, 
		len: 0 
	}; 
	for(var i=0; i < values.length; i++){
		reducedValue.count += values[i].count;	//total occurences
		reducedValue.len += values[i].len;		//total text length
	}
	return reducedValue;
}
