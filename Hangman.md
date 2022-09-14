# Hangman

Hangman is a popular word game. You will first see a set of spaces, each space representing a letter in a word:

<aside>
💡 _ _ _ _ _

</aside>

From the 26 letters in the alphabet, you pick one as your guess. Let’s say you picked “e”. Since there is an “e” in the word, it will be revealed on the game board and you will see:

<aside>
💡 _ _ _ _ e

</aside>

Feeling encouraged, you picked “p” for your next guess. Unfortunately, the word doesn’t have a “p”. So the game board remains unchanged:

<aside>
💡 _ _ _ _ e

</aside>

In the next turn, you guessed “t”. Aha, there are two “t”s. You will see both of them revealed:

<aside>
💡 t _ _ t e

</aside>

The game continues until you have guessed all letters correctly (in this case you win), or you have reached the maximum number of times you can guess (in this case you lose).

Now you want to write a program to help you make intelligent guesses to increase your chance to win. One strategy you think of is to always pick the most probable letter among the eligible words. A letter is most probable if it has the most occurrences among all letters.

Suppose the game designer has generously given you the entire word list. The game word is guaranteed to be drawn from that list.

You will then write a Python function:

```python
def guess_next_letter(pattern, used_letters=[], word_list=['about', 'abound', ...]):
    """Returns a letter from the alphabet.
    Input parameters:
				pattern: current state of the game board, with underscores "_" in the
            places of spaces (for example, "____e", that is, four underscores
            followed by 'e').
        used_letters: letters you have guessed in previous turns for the same
            word (for example, ['a', 'e', 's']).
        word_list: list of words from which the game word is drawn.
    """
		pass
```

Please complete the function. Don’t try hard to find the best strategy. Focus on implementing a strategy that works.

Once you are done with the implementation, please write a few unit test cases for your function to make sure it’s working as intended. Here is one example:

```python
def test_function_should_return_something():
	pattern = "____e"
	used_letters = list("abcde")
	word_list = [...]
	assert guess_next_letter(pattern, used_letters, word_list) is not None
```

Please create a new **public** repo on [Github](http://github.com) and commit all your files there. And then paste the URL to the repo to [https://airtable.com/shrv9JGF2fr6cbi9B](https://airtable.com/shrv9JGF2fr6cbi9B)