Ease of deployment / zero native DLLs → purely C# interpreters (MoonSharp, Lua-CSharp) have the advantage.
Performance & compatibility with existing Lua C modules → using a binding (NLua / Lua.NET) with real Lua gives you full speed and ability to call native Lua libraries (if you handle the DLLs).
