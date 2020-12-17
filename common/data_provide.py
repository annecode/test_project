#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne-home
# datetime: 2020-12-16 22:02
# filename: test_project/data_provide

import os
import json
import xlrd

paramfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data_param.xlsx')


class Param(object):
    def __init__(self, paramConf='{}'):
        self.paramConf = json.loads(paramConf)

    def paramRowsCount(self):
        pass

    def paramColsCount(self):
        pass

    def paramAllLine(self):
        pass

    def paramAllLineDict(self):
        pass


class XLS(Param):

    def __init__(self, paramConf):
        """
        :param paramConf: xls文件位置（绝对路径）
        """
        self.paramConf = paramConf
        self.paramfile = self.paramfile
        self.data = xlrd.open_workbook(self.paramfile)
        self.getParamSheet(self.paramConf['sheet'])

    def getParamSheet(self, nsheets):
        self.paramsheet = self.data.sheets()[nsheets]

    def getOneline(self, nRow):
        return self.paramsheet.row_values(nRow)

    def getOneCol(self, nCol):
        return self.paramsheet.col_values(nCol)

    def paramRowsCount(self):
        return self.paramsheet.nrows

    def paramColsCount(self):
        return self.paramsheet.ncols

    def paramHeader(self):
        return self.getOneline(1)

    def paramAlllineDict(self):
        nCountRows = self.paramRowsCount()
        nCountCols = self.paramColsCount()

        ParamAllListDict = {}
        iRowStep = 2
        iColStep = 0
        ParamHeader = self.paramHeader()

        while iRowStep < nCountRows:
            ParamOneLinelist = self.getOneline(iRowStep)
            ParamOnelineDict = {}

            while iColStep < nCountCols:
                ParamOnelineDict[ParamHeader[iColStep]] = ParamOneLinelist[iColStep]
                iColStep = iColStep + 1

            ParamAllListDict[iRowStep - 2] = ParamOnelineDict
            iRowStep = iRowStep + 1
            iColStep = 0

        return ParamAllListDict

    def paramAllline(self):
        nCountRows = self.paramRowsCount()
        paramall = []
        iRowStep = 2
        while iRowStep < nCountRows:
            paramall.append(self.getOneline(iRowStep))
        iRowStep = iRowStep + 1
        return paramall

    def __getParamCell(self, numberRow, numberCol):
        return self.paramsheet.cell_value(numberRow, numberCol)

    class ParamFactory(object):
        def chooseParam(self, type, paramConf):
            map = {
                'xlsx': XLS(paramConf),
            }
            return map[type]
