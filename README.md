# Kanto

```sh
$ conda install -c conda-forge rust
$ python setup.py build_ext
```


# Python interop

Milksnake: https://github.com/getsentry/milksnake

# C/C++ interop:

cbindgen: https://github.com/eqrion/cbindgen/blob/master/docs.md

# CMake interop:

Corrosion: https://github.com/corrosion-rs/corrosion


==================================

# WASM:

Build:

```sh
$ cd wasm/
$ wasm-pack build
$ cd www/
$ npm install
```

Run:

```
$ cd wasm/www/
$ npm run start
```

Rust WASM: https://rustwasm.github.io/docs/book/game-of-life/introduction.html
(Addtl. deps: https://rustwasm.github.io/wasm-pack/installer/)

### JavaScript introp

Example: https://webassembly.github.io/wabt/demo/wat2wasm/

```js
const wasmInstance = new WebAssembly.Instance(wasmModule, {});
const { addTwo } = wasmInstance.exports;
for (let i = 0; i < 10; i++) {
  console.log(addTwo(i, i));
}
```
