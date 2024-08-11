from cffi import FFI

ffi= FFI()

ffi.cdef("""
    struct lua_State;
    typedef struct lua_State lua_State;
             
    lua_State* luaL_newstate(void);
    void lua_close(lua_State*);
         
    void luaL_openlibs(lua_State*);
    void luaL_dofile(lua_State*, const char*);
""")

ffi.set_source('_lua_cffi', '''
    #include "lua/lua.h"
    #include "lua/lualib.h"
    #include "lua/lauxlib.h"
''', libraries=['lua'], library_dirs=['lua'])

if __name__ == '__main__':
    ffi.compile(verbose=1)
