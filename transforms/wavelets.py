import sys
sys.path.insert(1, '../')
import loader

path = "../images/frymire.png"



def main():
    img = loader.load_image(path)
    # loader.show_image(img)
    


if __name__ == "__main__":
    main()