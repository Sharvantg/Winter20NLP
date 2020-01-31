{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nltk.download()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nltk.corpus import brown"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['adventure',\n",
       " 'belles_lettres',\n",
       " 'editorial',\n",
       " 'fiction',\n",
       " 'government',\n",
       " 'hobbies',\n",
       " 'humor',\n",
       " 'learned',\n",
       " 'lore',\n",
       " 'mystery',\n",
       " 'news',\n",
       " 'religion',\n",
       " 'reviews',\n",
       " 'romance',\n",
       " 'science_fiction']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "brown.categories()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Dan', 'Morgan', 'told', 'himself', 'he', 'would', ...]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "brown.words(categories=\"adventure\")[:100]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Dan', 'Morgan', 'told', 'himself', 'he', 'would', ...]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "brown.words(categories=\"adventure\")[:100]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nltk.corpus import inaugural"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['1789-Washington.txt',\n",
       " '1793-Washington.txt',\n",
       " '1797-Adams.txt',\n",
       " '1801-Jefferson.txt',\n",
       " '1805-Jefferson.txt',\n",
       " '1809-Madison.txt',\n",
       " '1813-Madison.txt',\n",
       " '1817-Monroe.txt',\n",
       " '1821-Monroe.txt',\n",
       " '1825-Adams.txt',\n",
       " '1829-Jackson.txt',\n",
       " '1833-Jackson.txt',\n",
       " '1837-VanBuren.txt',\n",
       " '1841-Harrison.txt',\n",
       " '1845-Polk.txt',\n",
       " '1849-Taylor.txt',\n",
       " '1853-Pierce.txt',\n",
       " '1857-Buchanan.txt',\n",
       " '1861-Lincoln.txt',\n",
       " '1865-Lincoln.txt',\n",
       " '1869-Grant.txt',\n",
       " '1873-Grant.txt',\n",
       " '1877-Hayes.txt',\n",
       " '1881-Garfield.txt',\n",
       " '1885-Cleveland.txt',\n",
       " '1889-Harrison.txt',\n",
       " '1893-Cleveland.txt',\n",
       " '1897-McKinley.txt',\n",
       " '1901-McKinley.txt',\n",
       " '1905-Roosevelt.txt',\n",
       " '1909-Taft.txt',\n",
       " '1913-Wilson.txt',\n",
       " '1917-Wilson.txt',\n",
       " '1921-Harding.txt',\n",
       " '1925-Coolidge.txt',\n",
       " '1929-Hoover.txt',\n",
       " '1933-Roosevelt.txt',\n",
       " '1937-Roosevelt.txt',\n",
       " '1941-Roosevelt.txt',\n",
       " '1945-Roosevelt.txt',\n",
       " '1949-Truman.txt',\n",
       " '1953-Eisenhower.txt',\n",
       " '1957-Eisenhower.txt',\n",
       " '1961-Kennedy.txt',\n",
       " '1965-Johnson.txt',\n",
       " '1969-Nixon.txt',\n",
       " '1973-Nixon.txt',\n",
       " '1977-Carter.txt',\n",
       " '1981-Reagan.txt',\n",
       " '1985-Reagan.txt',\n",
       " '1989-Bush.txt',\n",
       " '1993-Clinton.txt',\n",
       " '1997-Clinton.txt',\n",
       " '2001-Bush.txt',\n",
       " '2005-Bush.txt',\n",
       " '2009-Obama.txt',\n",
       " '2013-Obama.txt',\n",
       " '2017-Trump.txt']"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inaugural.fileids()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Fellow',\n",
       " '-',\n",
       " 'Citizens',\n",
       " 'of',\n",
       " 'the',\n",
       " 'United',\n",
       " 'States',\n",
       " ':',\n",
       " 'In',\n",
       " 'compliance',\n",
       " 'with',\n",
       " 'a',\n",
       " 'custom',\n",
       " 'as',\n",
       " 'old',\n",
       " 'as',\n",
       " 'the',\n",
       " 'Government',\n",
       " 'itself',\n",
       " ',']"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inaugural.words(fileids='1861-Lincoln.txt')[:20]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['On',\n",
       " 'each',\n",
       " 'national',\n",
       " 'day',\n",
       " 'of',\n",
       " 'inauguration',\n",
       " 'since',\n",
       " '1789',\n",
       " ',',\n",
       " 'the',\n",
       " 'people',\n",
       " 'have',\n",
       " 'renewed',\n",
       " 'their',\n",
       " 'sense',\n",
       " 'of',\n",
       " 'dedication',\n",
       " 'to',\n",
       " 'the',\n",
       " 'United']"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inaugural.words(fileids='1941-Roosevelt.txt')[:20]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*** Introductory Examples for the NLTK Book ***\n",
      "Loading text1, ..., text9 and sent1, ..., sent9\n",
      "Type the name of the text or sentence to view it.\n",
      "Type: 'texts()' or 'sents()' to list the materials.\n",
      "text1: Moby Dick by Herman Melville 1851\n",
      "text2: Sense and Sensibility by Jane Austen 1811\n",
      "text3: The Book of Genesis\n",
      "text4: Inaugural Address Corpus\n"
     ]
    },
    {
     "ename": "LookupError",
     "evalue": "\n**********************************************************************\n  Resource \u001b[93mnps_chat\u001b[0m not found.\n  Please use the NLTK Downloader to obtain the resource:\n\n  \u001b[31m>>> import nltk\n  >>> nltk.download('nps_chat')\n  \u001b[0m\n  Attempted to load \u001b[93mcorpora/nps_chat\u001b[0m\n\n  Searched in:\n    - '/Users/sharvan/nltk_data'\n    - '/Applications/anaconda3/nltk_data'\n    - '/Applications/anaconda3/share/nltk_data'\n    - '/Applications/anaconda3/lib/nltk_data'\n    - '/usr/share/nltk_data'\n    - '/usr/local/share/nltk_data'\n    - '/usr/lib/nltk_data'\n    - '/usr/local/lib/nltk_data'\n**********************************************************************\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mLookupError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[0;32m/Applications/anaconda3/lib/python3.7/site-packages/nltk/corpus/util.py\u001b[0m in \u001b[0;36m__load\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     85\u001b[0m                 \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 86\u001b[0;31m                     \u001b[0mroot\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnltk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'{}/{}'\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msubdir\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mzip_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     87\u001b[0m                 \u001b[0;32mexcept\u001b[0m \u001b[0mLookupError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/Applications/anaconda3/lib/python3.7/site-packages/nltk/data.py\u001b[0m in \u001b[0;36mfind\u001b[0;34m(resource_name, paths)\u001b[0m\n\u001b[1;32m    698\u001b[0m     \u001b[0mresource_not_found\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'\\n%s\\n%s\\n%s\\n'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0msep\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msep\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 699\u001b[0;31m     \u001b[0;32mraise\u001b[0m \u001b[0mLookupError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresource_not_found\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    700\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mLookupError\u001b[0m: \n**********************************************************************\n  Resource \u001b[93mnps_chat\u001b[0m not found.\n  Please use the NLTK Downloader to obtain the resource:\n\n  \u001b[31m>>> import nltk\n  >>> nltk.download('nps_chat')\n  \u001b[0m\n  Attempted to load \u001b[93mcorpora/nps_chat.zip/nps_chat/\u001b[0m\n\n  Searched in:\n    - '/Users/sharvan/nltk_data'\n    - '/Applications/anaconda3/nltk_data'\n    - '/Applications/anaconda3/share/nltk_data'\n    - '/Applications/anaconda3/lib/nltk_data'\n    - '/usr/share/nltk_data'\n    - '/usr/local/share/nltk_data'\n    - '/usr/lib/nltk_data'\n    - '/usr/local/lib/nltk_data'\n**********************************************************************\n",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mLookupError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-37-a6ea6dd70c17>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mnltk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbook\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/Applications/anaconda3/lib/python3.7/site-packages/nltk/book.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     38\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text4:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtext4\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     39\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 40\u001b[0;31m \u001b[0mtext5\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mText\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnps_chat\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwords\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"Chat Corpus\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     41\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text5:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtext5\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     42\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/Applications/anaconda3/lib/python3.7/site-packages/nltk/corpus/util.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, attr)\u001b[0m\n\u001b[1;32m    121\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"LazyCorpusLoader object has no attribute '__bases__'\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    122\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 123\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__load\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    124\u001b[0m         \u001b[0;31m# This looks circular, but its not, since __load() changes our\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    125\u001b[0m         \u001b[0;31m# __class__ to something new:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/Applications/anaconda3/lib/python3.7/site-packages/nltk/corpus/util.py\u001b[0m in \u001b[0;36m__load\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     86\u001b[0m                     \u001b[0mroot\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnltk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'{}/{}'\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msubdir\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mzip_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     87\u001b[0m                 \u001b[0;32mexcept\u001b[0m \u001b[0mLookupError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 88\u001b[0;31m                     \u001b[0;32mraise\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     89\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     90\u001b[0m         \u001b[0;31m# Load the corpus.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/Applications/anaconda3/lib/python3.7/site-packages/nltk/corpus/util.py\u001b[0m in \u001b[0;36m__load\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     81\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     82\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 83\u001b[0;31m                 \u001b[0mroot\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnltk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'{}/{}'\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msubdir\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     84\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mLookupError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     85\u001b[0m                 \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/Applications/anaconda3/lib/python3.7/site-packages/nltk/data.py\u001b[0m in \u001b[0;36mfind\u001b[0;34m(resource_name, paths)\u001b[0m\n\u001b[1;32m    697\u001b[0m     \u001b[0msep\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'*'\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0;36m70\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    698\u001b[0m     \u001b[0mresource_not_found\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'\\n%s\\n%s\\n%s\\n'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0msep\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msep\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 699\u001b[0;31m     \u001b[0;32mraise\u001b[0m \u001b[0mLookupError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresource_not_found\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    700\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    701\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mLookupError\u001b[0m: \n**********************************************************************\n  Resource \u001b[93mnps_chat\u001b[0m not found.\n  Please use the NLTK Downloader to obtain the resource:\n\n  \u001b[31m>>> import nltk\n  >>> nltk.download('nps_chat')\n  \u001b[0m\n  Attempted to load \u001b[93mcorpora/nps_chat\u001b[0m\n\n  Searched in:\n    - '/Users/sharvan/nltk_data'\n    - '/Applications/anaconda3/nltk_data'\n    - '/Applications/anaconda3/share/nltk_data'\n    - '/Applications/anaconda3/lib/nltk_data'\n    - '/usr/share/nltk_data'\n    - '/usr/local/share/nltk_data'\n    - '/usr/lib/nltk_data'\n    - '/usr/local/lib/nltk_data'\n**********************************************************************\n"
     ]
    }
   ],
   "source": [
    "from nltk.book import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'FreqDist' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-39-956f2bb847db>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mf\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0mFreqDist\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtext1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'FreqDist' is not defined"
     ]
    }
   ],
   "source": [
    "f= FreqDist(text1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nltk.probability import FreqDist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'text1' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-46-956f2bb847db>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mf\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0mFreqDist\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtext1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'text1' is not defined"
     ]
    }
   ],
   "source": [
    "f= FreqDist(text1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*** Introductory Examples for the NLTK Book ***\n",
      "Loading text1, ..., text9 and sent1, ..., sent9\n",
      "Type the name of the text or sentence to view it.\n",
      "Type: 'texts()' or 'sents()' to list the materials.\n",
      "text1: Moby Dick by Herman Melville 1851\n",
      "text2: Sense and Sensibility by Jane Austen 1811\n",
      "text3: The Book of Genesis\n",
      "text4: Inaugural Address Corpus\n"
     ]
    },
    {
     "ename": "LookupError",
     "evalue": "\n**********************************************************************\n  Resource \u001b[93mnps_chat\u001b[0m not found.\n  Please use the NLTK Downloader to obtain the resource:\n\n  \u001b[31m>>> import nltk\n  >>> nltk.download('nps_chat')\n  \u001b[0m\n  Attempted to load \u001b[93mcorpora/nps_chat\u001b[0m\n\n  Searched in:\n    - '/Users/sharvan/nltk_data'\n    - '/Applications/anaconda3/nltk_data'\n    - '/Applications/anaconda3/share/nltk_data'\n    - '/Applications/anaconda3/lib/nltk_data'\n    - '/usr/share/nltk_data'\n    - '/usr/local/share/nltk_data'\n    - '/usr/lib/nltk_data'\n    - '/usr/local/lib/nltk_data'\n**********************************************************************\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mLookupError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[0;32m/Applications/anaconda3/lib/python3.7/site-packages/nltk/corpus/util.py\u001b[0m in \u001b[0;36m__load\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     85\u001b[0m                 \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 86\u001b[0;31m                     \u001b[0mroot\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnltk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'{}/{}'\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msubdir\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mzip_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     87\u001b[0m                 \u001b[0;32mexcept\u001b[0m \u001b[0mLookupError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/Applications/anaconda3/lib/python3.7/site-packages/nltk/data.py\u001b[0m in \u001b[0;36mfind\u001b[0;34m(resource_name, paths)\u001b[0m\n\u001b[1;32m    698\u001b[0m     \u001b[0mresource_not_found\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'\\n%s\\n%s\\n%s\\n'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0msep\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msep\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 699\u001b[0;31m     \u001b[0;32mraise\u001b[0m \u001b[0mLookupError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresource_not_found\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    700\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mLookupError\u001b[0m: \n**********************************************************************\n  Resource \u001b[93mnps_chat\u001b[0m not found.\n  Please use the NLTK Downloader to obtain the resource:\n\n  \u001b[31m>>> import nltk\n  >>> nltk.download('nps_chat')\n  \u001b[0m\n  Attempted to load \u001b[93mcorpora/nps_chat.zip/nps_chat/\u001b[0m\n\n  Searched in:\n    - '/Users/sharvan/nltk_data'\n    - '/Applications/anaconda3/nltk_data'\n    - '/Applications/anaconda3/share/nltk_data'\n    - '/Applications/anaconda3/lib/nltk_data'\n    - '/usr/share/nltk_data'\n    - '/usr/local/share/nltk_data'\n    - '/usr/lib/nltk_data'\n    - '/usr/local/lib/nltk_data'\n**********************************************************************\n",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mLookupError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-48-a6ea6dd70c17>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mnltk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbook\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/Applications/anaconda3/lib/python3.7/site-packages/nltk/book.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     38\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text4:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtext4\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     39\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 40\u001b[0;31m \u001b[0mtext5\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mText\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnps_chat\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwords\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"Chat Corpus\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     41\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"text5:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtext5\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     42\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/Applications/anaconda3/lib/python3.7/site-packages/nltk/corpus/util.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, attr)\u001b[0m\n\u001b[1;32m    121\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"LazyCorpusLoader object has no attribute '__bases__'\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    122\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 123\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__load\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    124\u001b[0m         \u001b[0;31m# This looks circular, but its not, since __load() changes our\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    125\u001b[0m         \u001b[0;31m# __class__ to something new:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/Applications/anaconda3/lib/python3.7/site-packages/nltk/corpus/util.py\u001b[0m in \u001b[0;36m__load\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     86\u001b[0m                     \u001b[0mroot\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnltk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'{}/{}'\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msubdir\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mzip_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     87\u001b[0m                 \u001b[0;32mexcept\u001b[0m \u001b[0mLookupError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 88\u001b[0;31m                     \u001b[0;32mraise\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     89\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     90\u001b[0m         \u001b[0;31m# Load the corpus.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/Applications/anaconda3/lib/python3.7/site-packages/nltk/corpus/util.py\u001b[0m in \u001b[0;36m__load\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     81\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     82\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 83\u001b[0;31m                 \u001b[0mroot\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnltk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'{}/{}'\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msubdir\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     84\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mLookupError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     85\u001b[0m                 \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/Applications/anaconda3/lib/python3.7/site-packages/nltk/data.py\u001b[0m in \u001b[0;36mfind\u001b[0;34m(resource_name, paths)\u001b[0m\n\u001b[1;32m    697\u001b[0m     \u001b[0msep\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'*'\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0;36m70\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    698\u001b[0m     \u001b[0mresource_not_found\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'\\n%s\\n%s\\n%s\\n'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0msep\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msep\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 699\u001b[0;31m     \u001b[0;32mraise\u001b[0m \u001b[0mLookupError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresource_not_found\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    700\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    701\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mLookupError\u001b[0m: \n**********************************************************************\n  Resource \u001b[93mnps_chat\u001b[0m not found.\n  Please use the NLTK Downloader to obtain the resource:\n\n  \u001b[31m>>> import nltk\n  >>> nltk.download('nps_chat')\n  \u001b[0m\n  Attempted to load \u001b[93mcorpora/nps_chat\u001b[0m\n\n  Searched in:\n    - '/Users/sharvan/nltk_data'\n    - '/Applications/anaconda3/nltk_data'\n    - '/Applications/anaconda3/share/nltk_data'\n    - '/Applications/anaconda3/lib/nltk_data'\n    - '/usr/share/nltk_data'\n    - '/usr/local/share/nltk_data'\n    - '/usr/lib/nltk_data'\n    - '/usr/local/lib/nltk_data'\n**********************************************************************\n"
     ]
    }
   ],
   "source": [
    "from nltk.book import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "f= FreqDist(text1)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
