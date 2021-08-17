this model will create a table with various entries.
the purpose of this app is to test how lookup times scale with table size.
other structures might be explored


questions:
    is .git(pk = <primary key>) constant time?
    is .filter(<CharField> = <search term>) O(n) time w.r.t table length