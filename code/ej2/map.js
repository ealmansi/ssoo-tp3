function() {
	var stopwords = ["a", "able", "about", "across", "after", "all", "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at", "be", "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do", "does", "either", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have", "he", "her", "hers", "him", "his", "how", "however", "i", "if", "in", "into", "is", "it", "its", "just", "least", "let", "like", "likely", "may", "me", "might", "most", "must", "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or", "other", "our", "own", "rather", "said", "say", "says", "she", "should", "since", "so", "some", "than", "that", "the", "their", "them", "then", "there", "these", "they", "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "would", "yet", "you", "your", "br"];
	var words = this.text.split(" ");	//array of words from text
	if(words){	//not empty array
		for(var i=0; i < words.length; i++){
			var word = words[i].toLowerCase().replace(/[^a-zA-Z 0-9]+/g,'');	//words in lower case, without puntuation and special chars
			if(stopwords.indexOf(word) == -1 && word){	//not stop word or empty word
				value = {s1: 0, s2: 0, s3: 0, s4: 0, s5: 0};	//count for each score
				var index = this.score;
				if(index == 1){
					value.s1 = 1;
				}				
				else if(index == 2){
					value.s2 =1;
				}
				else if(index == 3){
					value.s3 =1;
				}
				else if(index == 4){
					value.s4 =1;
				}
				else{
					value.s5 =1;
				}
				emit(word,value);
			}
		}
	}
}
