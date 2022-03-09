def spin_words(sentense):
	final_str = ''
	str = sentense.split(' ')
	for word in str:
		len_wd = len(word)
		if len_wd >= 5:
			tmp = word[::-1]
		else:
			tmp = word
		final_str += tmp + ' '
	return (final_str)

def main():
	print(spin_words("Welcome in the hell ZUBOSTAT"))

if __name__ == "__main__":
    main()