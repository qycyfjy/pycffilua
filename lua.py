from _lua_cffi import ffi, lib

L = lib.luaL_newstate()
lib.luaL_openlibs(L)
lib.luaL_dofile(L, b"test.lua")
lib.lua_close(L)
