import type { Product } from '@/lib/types';

export function ProductsTable({ products }: { products: Product[] }) {
  return (
    <section className="panel">
      <div className="panel-heading">
        <div>
          <h2>Dữ liệu sản phẩm mẫu</h2>
          <p>Bot đang đọc từ file CSV trong data/shop/products.csv.</p>
        </div>
      </div>
      <div className="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Tên sản phẩm</th>
              <th>Danh mục</th>
              <th>Giá</th>
              <th>Tồn kho</th>
              <th>Use case</th>
            </tr>
          </thead>
          <tbody>
            {products.map((product) => (
              <tr key={product.id}>
                <td>{product.name}</td>
                <td>{product.category}</td>
                <td>{product.formatted_price}</td>
                <td>{product.stock}</td>
                <td>{product.use_cases}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
