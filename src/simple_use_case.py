import dill

def gen():
    x = yield "hello"
    print(x)

if __name__ == "__main__":
    g = gen()
    print(next(g))
    try:
        gen_bytes = dill.dumps(g)
    except TypeError as e:
        # generator object is not serializable
        print(f"Processing error: {e}")
