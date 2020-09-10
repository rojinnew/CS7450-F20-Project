# -*- coding: utf-8 -*-
"""
	File name: catgeory_structure.py
	Authors: Rojin Aei
	Date created: 9/9/2020
	Date last modified: 9/9/2020
	Python Version: 3.8.1
	Execute: $ [python3.8] category_structure.py
	Usage: Gives sample usage of `Wikipedia API` for categories
    Resource: https://github.com/martin-majlis/Wikipedia-API
"""
import wikipediaapi
import pandas as pd

def print_categorymembers(categorymembers, level, max_level, levels, prev):
    """parsing the result and create a hierarchy."""
    print("level", level)
    print("max level", max_level)
    idx = 0
    for cat in categorymembers.values():
        print("%s %s (ns: %d)" % ("*" * (level + 1), cat.title, cat.ns))
        levels[level] += [prev + "."+ str(idx)+ "." +cat.title]
        idx += 1
        if cat.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
            print_categorymembers(cat.categorymembers, level + 1, max_level, levels, \
                                  prev + "."+ str(idx-1))

if __name__ == "__main__":
    wiki_wiki = wikipediaapi.Wikipedia("en")
    category = wiki_wiki.page("Category:Physics")
    #category = wiki_wiki.page("Category:Fictional_characters_by_behavior")
    ROOT_SYMBOL = "*"
    LEVELS = {}
    MAX_LEVEL = 1
    LEVEL = 0
    for i in range(0, MAX_LEVEL+1):
        LEVELS[i] = []
    print_categorymembers(category.categorymembers, LEVEL, MAX_LEVEL, LEVELS, ROOT_SYMBOL)
    for i in range(0, MAX_LEVEL+1):
        pd.DataFrame.from_dict(LEVELS[i]).to_csv("output_category/level"+str(i)+".csv", index=False)
