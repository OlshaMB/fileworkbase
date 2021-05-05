from distutils.core import setup, Extension
def main():
    setup(name="fileworkbase",
          version="0.1.0",
          description="Python interface for the filebase",
          author="OlshaMB",
          author_email="your_email@gmail.com",
          ext_modules=[Extension("fileworkbase", ["fileworkbase.cpp"])])
if __name__ == '__main__':
    main()