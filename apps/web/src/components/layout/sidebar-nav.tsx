'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Bot, LayoutDashboard, MessageSquareText } from 'lucide-react';

const navItems = [
  {
    title: 'Dashboard',
    href: '/dashboard',
    icon: LayoutDashboard,
  },
  {
    title: 'Chat thử',
    href: '/chat',
    icon: MessageSquareText,
  },
];

export function SidebarNav() {
  const pathname = usePathname();

  return (
    <aside className="sidebar">
      <Link className="brand" href="/dashboard" aria-label="MeowAI Dashboard">
        <span className="brand-mark">M</span>
        <span>
          <strong>MeowAI</strong>
          <small>Bot Studio</small>
        </span>
      </Link>

      <nav className="nav-list" aria-label="Điều hướng chính">
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = pathname === item.href;

          return (
            <Link key={item.href} className={`nav-link ${isActive ? 'active' : ''}`} href={item.href}>
              <Icon size={18} />
              <span>{item.title}</span>
            </Link>
          );
        })}
      </nav>

      <div className="sidebar-footer">
        <Bot size={18} />
        <span>Phase 1</span>
      </div>
    </aside>
  );
}
