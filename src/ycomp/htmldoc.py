# -*- coding: utf-8 -*-

from re import sub as resub

class DomTree:
    def __init__(self, dtree, output):
        self.output = output
        self.dtree = dtree

    def create_element(self, elem):
        ind = '  ' * elem['indent']
        s = f'{ind}<{elem["tag"]}'
        if elem['attrs'] != None:
            sa = []
            for a in elem['attrs']:
                sa.append(f'{a[0]}="{a[1]}"')
            attrs = ' ' + ' '.join(sa)
            s += attrs

        txt = ''
        if elem['text'] != None:
            txt = f'{ind}  {elem["text"]}\n'
        closing = f'>\n{txt}'
        s += closing
        return s

    def close_tag(self, tag, ind):
        i = '  ' * ind
        s = f'{i}</{tag}>\n'
        return s

    def create_doc(self):
        f = open(self.output, 'a')
        ltree = len(self.dtree)

        s = '<!DOCTYPE html>\n'
        f.write(s)

        #indstack = [0]
        indsz = 0
        tagstack = []
        started = False

        for i in range(1, ltree):
            s = ''
            line = self.dtree[i]
            curind = line['indent']
            curtag = line["tag"]

            if not started:
                started = True
                newtag = (curtag, line['autoclose'])
                tagstack.append(newtag)
                tmp = self.create_element(line)
                f.write(tmp)
                indsz = curind
            else:
                if curind > indsz:
                    newtag = (curtag, line['autoclose'])
                    tagstack.append(newtag)
                    tmp = self.create_element(line)
                    f.write(tmp)
                    indsz = curind
                    continue

                if curind < indsz:
                    tmp_ind = indsz
                    #tmp_pop = curind - 1
                    #for n in range(0, indsz):
                    while tmp_ind >= curind:
                        tmp_ind -= 1
                        if len(tagstack) > 0:
                            t = tagstack.pop()
                            tclose = None
                            if t[1] == 1:
                                tclose = self.close_tag(t[0], curind)
                                f.write(tclose)

                    newtag = (curtag, line['autoclose'])
                    tagstack.append(newtag)
                    tmp = self.create_element(line)
                    f.write(tmp)

                    indsz = curind
                    continue

                if curind == indsz:
                    t = tagstack.pop()
                    tclose = None
                    if t[1] == 1:
                        tclose = self.close_tag(t[0], curind)
                        f.write(tclose)

                    newtag = (curtag, line['autoclose'])
                    tagstack.append(newtag)
                    tmp = self.create_element(line)
                    f.write(tmp)
                    indsz = curind
                    continue

        lind = indsz
        while True:
            if len(tagstack) == 0:
                break
            t = tagstack.pop()
            tclose = None
            if t[1] == 1:
                tclose = self.close_tag(t[0], lind)
                f.write(tclose)
            lind -= 1

        f.close()
