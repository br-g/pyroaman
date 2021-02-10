<img src="https://raw.githubusercontent.com/br-g/pyroaman/main/artwork/logo.png" height=100px style="margin-bottom: -14px;">

Pyroaman helps you explore Roam Research databases with Python.


## Installation

You need Python 3.6 or later to use Pyroaman.    
Install and update using pip:

    $ pip install -U pyroaman


## A Simple Example

First, you need the JSON export of a Roam database.    
For this demo, we will use a public one: `roamhacker`.

    $ curl https://raw.githubusercontent.com/br-g/roam-public-db/main/json/roamhacker.json -o roamhacker.json


#### Load

```python
import pyroaman

db = pyroaman.load('roamhacker.json')
print(db)
```
```
Database (276 pages, 2397 blocks)
``` 

#### Lookup

Let's query blocks that contain the word "agile":

```python
some_blocks = db.lookup('agile')
print(some_blocks)
```
```
[Block (string: "Goal for myself: Fight desire to...", is_page: False, children: 1, links: 1, backlinks: 0),
 Block (string: "Agile Note Taking", is_page: True, children: 0, links: 0, backlinks: 1),
 Block (string: "[9]  This example comes from Nas...", is_page: False, children: 0, links: 0, backlinks: 0)]
```

#### Explore

 Get the text of a block (its string without images, references...):
```python
print(some_blocks[0].text)
```
```
'Goal for myself: Fight desire to have the "perfect system". Better to use and iterate improvements, rather than wait for perfect system. And by the way, is there a perfect system? Agile Note Taking?? - sprint, try, iterate'
```

Get the children of a block:
```python
print(some_blocks[0].children)
```
```
[Block (string: "Open organization: disorder with...", is_page: False, children: 0, links: 0, backlinks: 0)]
```

Get its links:
```python
print(some_blocks[0].links)
```
```
[Block (string: "Agile Note Taking", is_page: True, children: 0, links: 0, backlinks: 1)]
```

Get backlinks:
```python
print(some_blocks[1].backlinks)
```
```
[Block (string: "Goal for myself: Fight desire to...", is_page: False, children: 1, links: 1, backlinks: 0)]
```

Get block's metadata:
```python
print(some_blocks[0].metadata)
```
```
{'edit-time': 1606399607792,
 'refs': [{'uid': 'YAYZKdubo'}],
 'uid': 'XP9lZauAg',
 ':block/refs': [{':block/uid': 'YAYZKdubo'}],
 ':create/user': {':user/uid': 'kfmqimzFiIOQwL1xgoBOApXxsup1'},
 'create-time': 1599461612984,
 ':edit/user': {':user/uid': 'kfmqimzFiIOQwL1xgoBOApXxsup1'}}
```
