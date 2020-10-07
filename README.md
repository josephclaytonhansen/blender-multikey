# blender-multikey
# MultiKey for Blender 2.8+ 
## currently in beta, public release planned for early November
[![Screen-Shot-2020-10-07-at-1-45-38-PM.png](https://i.postimg.cc/7h7TxdmT/Screen-Shot-2020-10-07-at-1-45-38-PM.png)](https://postimg.cc/rRVpjn68)
### What does MultiKey do?
MultiKey allows all objects in a set collection to have the same shape key applied at once; i.e., the value of "key1" can be changed for objects 1, 2, and 3 in a collection with just two clicks. Practically speaking, this means you could have an eyebrow object, eyelid object, and face object, each with a "raised eyebrow" key. You could change the values of all these "raised eyebrow" keys all at once. You can do this with up to five separate keys, which can be enabled/disabled with checkboxes. _Future releases will have keyframing functionality and connect to the NLA for animation purposes. _
### Where do I find it?
MultiKey lives in the Properties in its own tab. 

### How do I use it?
First, create a collection that all the related objects are in. _Future releases will allow for collection selection._ Each object in the collection must have at least one shape key. Give objects shape keys with exactly the same names. Open MultiKey, type in the key name, set the value, and click "Preview". The checkbox to the right of each key allows it be enabled/disabled.

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
