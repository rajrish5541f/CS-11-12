from tkinter import *
root=Tk()

thedict = {
    "apple": "A round fruit with red or green skin and a sweet taste.",
    "ball": "A round object used in games and sports.",
    "cat": "A small domesticated carnivorous mammal with soft fur.",
    "dog": "A domesticated carnivorous mammal often kept as a pet.",
    "elephant": "A large mammal with a trunk, known for its size and intelligence.",
    "fish": "A cold-blooded animal that lives in water and has fins.",
    "grape": "A small, round, smooth-skinned fruit, typically purple or green.",
    "hat": "A head covering, often with a brim.",
    "ice": "Frozen water, a solid state of water.",
    "jelly": "A soft, sweet food made from fruit juice and sugar.",
    "kite": "A lightweight framework covered with cloth or plastic, flown in the wind at the end of a long string.",
    "lemon": "A yellow citrus fruit with a tart taste.",
    "moon": "The natural satellite of the Earth, visible by reflected light from the sun.",
    "nest": "A structure built by birds to lay eggs and raise their young.",
    "orange": "A round, juicy citrus fruit with a tough skin.",
    "pencil": "A writing or drawing instrument with a thin stick of graphite inside.",
    "queen": "The female ruler of an independent state, especially one who inherits the position by right of birth.",
    "rain": "Water droplets that fall from clouds in the sky.",
    "sun": "The star at the center of our solar system, which provides light and heat to the Earth.",
    "tree": "A perennial plant with a trunk, branches, and leaves.",
    "umbrella": "A device used for protection from the rain or sun, consisting of a fabric covering stretched over a collapsible frame.",
    "vase": "A container, typically made of glass or ceramic, used for holding cut flowers or for decoration.",
    "window": "An opening in the wall of a building, usually fitted with glass, that allows light and air to enter.",
    "xylophone": "A musical instrument made of wooden bars that are struck with mallets.",
    "yogurt": "A food made from milk that has been fermented, often flavored and sweetened.",
    "zebra": "An African wild horse with black-and-white stripes and an erect mane."
}

def ans():
    ex =Label(root, text=' ')
    ex.grid(row=2, column=0)
    ex.grid_remove()
    print(type(ex))
    if box.get()=='':
            Label(root, text="Please enter something!").grid(row=2, column=0)
            return None
    else:
        for i in thedict.keys():
            if box.get()==i:
                Label(root, text=thedict.get(box.get())).grid(row=2, column=0)
                break
        else:
            Label(root, text="Not found!").grid(row=2, column=0)
    
        
box=Entry(root, width=50)
box.grid(row=0, column=0)
but=Button(root, text='Search', command=ans)
but.grid(row=1, column=0)

root.mainloop()