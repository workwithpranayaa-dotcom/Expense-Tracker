import "./globals.css";
export const metadata = { title: "shopforge", description: "A commerce operations system covering storefront concerns plus inventory, order workflows, customers and operational analytics." };
export default function RootLayout({children}:{children:React.ReactNode}) {
  return <html lang="en"><body>{children}</body></html>;
}