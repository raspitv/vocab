# vocab test by Alex Eames of RasPi.TV Shared under CC BY-SA 3.0 license
[CC-BY-NC-SA 3.0 license](https://creativecommons.org/licenses/by-nc-sa/3.0/)

This was designed for testing your vocabulary

I've blogged about it here...
http://raspi.tv/?p=9652

To run this on your Pi...

git clone https://github.com/raspitv/vocab/

cd vocab

python3 vocab.py

Then it will When you run the script it will display a word on the screen. Your job is to hit “Enter” if you can define that word. I’m strict here – if you can define it, you know it. If you can’t define it, you don’t know it. If you can guess it, but have never come across it before – you still don’t know it.

So if you can define the word, you hit “Enter”. If you can’t, you hit any other key and then “Enter”. The script will show you 100 random words and calculate your score according to that.

If you want to change the number of words asked, change the value of iterations in line 5. A larger value will give more accuracy at the expense of time.

