import numpy as np
import pytest

import ibis
import ibis.expr.datatypes as dt
import ibis.expr.operations as ops
import ibis.expr.rules as rlz
import ibis.expr.types as ir
from ibis.common.exceptions import IbisTypeError


def test_operation():
    class Log(ops.Node):
        arg = rlz.double()
        base = rlz.optional(rlz.double())

    Log(1, base=2)
    Log(1, base=2)
    Log(arg=10)


def test_ops_smoke():
    expr = ir.literal(3)
    ops.Cast(expr, to='int64')
    ops.TypeOf(arg=2)
    ops.Negate(4)
    ops.Negate(4.0)
    ops.NullIfZero(0)
    ops.NullIfZero(1)
    ops.IsNull(ir.null())
    ops.NotNull(ir.null())
    ops.ZeroIfNull(ir.null())
    ops.IfNull(1, ops.NullIfZero(0).to_expr())
    ops.NullIf(ir.null(), ops.NullIfZero(0).to_expr())
    ops.IsNan(np.nan)
    ops.IsInf(np.inf)
    ops.Ceil(4.5)
    ops.Floor(4.5)
    ops.Round(3.43456)
    ops.Round(3.43456, 2)
    ops.Round(3.43456, digits=1)
    ops.Clip(123, lower=30)
    ops.Clip(123, lower=30, upper=100)
    ops.BaseConvert('EEE', from_base=16, to_base=10)
    ops.Logarithm(100)
    ops.Log(100)
    ops.Log(100, base=2)
    ops.Ln(100)
    ops.Log2(100)
    ops.Log10(100)
    ops.Uppercase('asd')
    ops.Lowercase('asd')
    ops.Reverse('asd')
    ops.Strip('asd')
    ops.LStrip('asd')
    ops.RStrip('asd')
    ops.Capitalize('asd')
    ops.Substring('asd', start=1)
    ops.Substring('asd', 1)
    ops.Substring('asd', 1, length=2)
    ops.StrRight('asd', nchars=2)
    ops.Repeat('asd', times=4)
    ops.StringFind('asd', 'sd', start=1)
    ops.Translate('asd', from_str='bd', to_str='ce')
    ops.LPad('asd', length=2, pad='ss')
    ops.RPad('asd', length=2, pad='ss')
    ops.StringJoin(',', ['asd', 'bsdf'])
    ops.FuzzySearch('asd', pattern='n')
    ops.StringSQLLike('asd', pattern='as', escape='asd')
    ops.RegexExtract('asd', pattern='as', index=1)
    ops.RegexReplace('asd', 'as', 'a')
    ops.StringReplace('asd', 'as', 'a')
    ops.StringSplit('asd', 's')
    ops.StringConcat(['s', 'e'])
    ops.StartsWith('asd', 'as')
    ops.EndsWith('asd', 'xyz')


def test_instance_of_operation():
    class MyOperation(ops.Node):
        arg = rlz.instance_of(ir.IntegerValue)

    MyOperation(ir.literal(5))

    with pytest.raises(IbisTypeError):
        MyOperation(ir.literal('string'))


def test_array_input():
    class MyOp(ops.Value):
        value = rlz.value(dt.Array(dt.double))
        output_dtype = rlz.dtype_like('value')
        output_shape = rlz.shape_like('value')

    raw_value = [1.0, 2.0, 3.0]
    op = MyOp(raw_value)
    result = op.value
    expected = ibis.literal(raw_value)
    assert result.equals(expected)


def test_custom_table_expr():
    class MyTable(ir.Table):
        pass

    class SpecialTable(ops.DatabaseTable):
        @property
        def output_type(self):
            return MyTable

    con = ibis.pandas.connect({})
    node = SpecialTable('foo', ibis.schema([('a', 'int64')]), con)
    expr = node.to_expr()
    assert isinstance(expr, MyTable)


@pytest.mark.parametrize(
    ['file_format', 'extension'],
    [
        (ops.ArrowFileFormat(), 'arrow'),
        (ops.CsvFileFormat(delimiter=','), 'csv'),
        (ops.OrcFileFormat(), 'orc'),
        (ops.ParquetFileFormat(), 'parquet'),
    ],
)
def test_file_table(file_format, extension):
    node = ops.FileTable(
        items=[
            f's3://foo/2009/01/data.{extension}',
            f's3://foo/2009/02/data.{extension}',
        ],
        schema=ibis.schema(
            [
                ('a', 'int32'),
            ]
        ),
        file_format=file_format,
    )
    assert str(node.to_expr())

    with pytest.raises(ValueError, match='Missing URI scheme'):
        node = ops.FileTable(
            items=[f'foo/bar/baz.{extension}'],
            schema=node.schema,
            file_format=file_format,
        )


def test_file_table_format():
    formats = [
        ops.ArrowFileFormat(),
        ops.CsvFileFormat(delimiter=','),
        ops.CsvFileFormat(delimiter='\t'),
        ops.OrcFileFormat(),
        ops.ParquetFileFormat(),
    ]
    for idx1, format1 in enumerate(formats):
        for idx2, format2 in enumerate(formats):
            if idx1 == idx2:
                assert format1 == format2
            else:
                assert format1 != format2


@pytest.fixture(scope='session')
def dummy_op():
    class DummyOp(ops.Value):
        arg = rlz.any

    return DummyOp


def test_too_many_args_not_allowed(dummy_op):
    with pytest.raises(TypeError):
        dummy_op(1, 2)


def test_too_few_args_not_allowed(dummy_op):
    with pytest.raises(TypeError):
        dummy_op()


def test_operation_class_aliases():
    assert ops.ValueOp is ops.Value
    assert ops.UnaryOp is ops.Unary
    assert ops.BinaryOp is ops.Binary
    assert ops.WindowOp is ops.Window
    assert ops.AnalyticOp is ops.Analytic


def test_expression_class_aliases():
    assert ir.TableExpr is ir.Table
    assert ir.AnalyticExpr is ir.Analytic
    assert ir.ExistsExpr is ir.Exists
    assert ir.TopKExpr is ir.TopK
    assert ir.ValueExpr is ir.Value
    assert ir.ScalarExpr is ir.Scalar
    assert ir.ColumnExpr is ir.Column
    assert ir.AnyValue is ir.Value
    assert ir.AnyScalar is ir.Scalar
    assert ir.AnyColumn is ir.Column
    assert ir.ListExpr is ir.ValueList
