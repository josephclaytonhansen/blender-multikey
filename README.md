# blender-multikey
# MultiKey for Blender 2.8+ 
## currently in beta, public release planned for early November
[![Screen-Shot-2020-10-07-at-3-01-19-PM.png](https://i.postimg.cc/QMyhxq4Q/Screen-Shot-2020-10-07-at-3-01-19-PM.png)](https://postimg.cc/Z9p1w6hn)
### What does MultiKey do?
MultiKey allows all objects in a set collection to have the same shape key applied at once.

For example, this means you could have an eyebrow object, eyelid object, and face object, each with a "raised eyebrow" key. You could change the values of all these "raised eyebrow" keys all at once. You can do this with up to five separate keys, which can be enabled/disabled with checkboxes. 

MultiKey allows you to select the collection that the objects are in. It also allows up to 5 shape keys to be adjusted at a time. It also has a "reset to 0", "reset to 1", and a "set all to" that allows the 5 shape keys to be changed as one. 

### Where do I find it?
MultiKey lives in the Properties in its own tab. 

### How do I use it?
_Check the wiki for detailed instructions._
First, create a collection that all the related objects are in. Each object in the collection must have at least one shape key. Give objects shape keys with exactly the same names. Open MultiKey, type in the key name, set the value, and click "Preview". The checkbox to the right of each key allows it be enabled/disabled.

### Planned release features
* Add keyframes
* Select collection
* ~~Preview/add multiple keys at once~~ commit 6928382

### Features beyond release (1.0+)
* None planned

### Bugs/feature requests: 
* ~~If you have an object selected when you click Preview, it will be de-selected.~~ commit 5d5c2e9

Send bugs or feature requests to josephclaytonhansen@gmail.com. Donations greatly appreciated!

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/G2G216RHJ)
