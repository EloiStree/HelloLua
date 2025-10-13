from lupa import LuaRuntime

lua = LuaRuntime(unpack_returned_tuples=True)
lua.execute('print("Hello World")')  # Print Hello World in Lua

result = lua.eval('2 + 3 * 5')
print(result)  # → 17

lua_func = lua.eval('function(x, y) return x + y end')
print(lua_func(10, 20))  # → 30
