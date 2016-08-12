import os
import glob
import json

import stencil


for fn in glob.glob('tmpl/*.tpl'):
    print fn,
    base, ext = os.path.splitext(fn)
    with open(fn, 'r') as fin:
        src = fin.read()

    with open(base + '.out', 'r') as fin:
        out = fin.read()

    with open(base + '.json', 'r') as fin:
        data = json.load(fin)

    c = stencil.Context(**data)
    t = stencil.Template(src)
    result = t.render(c)

    assert result == out, "Mismatched output for %r\n%r\n%r" % (fn, out, result)
    print "OK"