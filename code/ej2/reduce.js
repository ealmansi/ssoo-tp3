function (key, values) { 
	reducedValue = {s1: 0, s2: 0, s3: 0, s4: 0, s5: 0};
	for(var i=0; i < values.length; i++){	//total occurrences for words
		reducedValue.s1 += values[i].s1;
		reducedValue.s2 += values[i].s2;
		reducedValue.s3 += values[i].s3;
		reducedValue.s4 += values[i].s4;
		reducedValue.s5 += values[i].s5;
	}
	return reducedValue;
}
