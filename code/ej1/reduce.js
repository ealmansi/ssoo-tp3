function (key, values) { 
	reducedValue = {
		count: 0,
		score: 0,
	};
    for (var i=0; i < values.length; i++){
        reducedValue.count += values[i].count;	//total ocurrences
		reducedValue.score += values[i].score;	//total score
    }
    return reducedValue;
}
