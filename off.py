from lib.tree import RGBXmasTree

tree = RGBXmasTree()
try:
    tree.off()
finally:
    tree.close()
