Visualize PyTorch 2.0 IRs in one place
![Screenshot 2023-03-20 at 4 56 46 PM](https://user-images.githubusercontent.com/3282513/226496067-c2b8bf1d-59e5-45ed-a022-af12139d000e.png)



# Usage

1. Make sure `npm --version` > 16
2. `make dev`
3. Go to http://python.localhost:10240/
4. Input your PyTorch code

# TODO

1. Dynamo
2. Triton
3. PTX
4. Inductor pre and post fusion IR
5. Aten IR
6. Preserve stack trace information
7. Do all of the above without asking users to add print statements
8. See if godbolt team is open to us having a pytorch dependency otherwise will need to create our own instance
