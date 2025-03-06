import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatTreeModule } from '@angular/material/tree';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatMenuModule } from '@angular/material/menu';
import { Router } from '@angular/router';

@Component({
  selector: 'app-nav-bar',
  imports: [
    MatButtonModule,
    MatIconModule,
    MatMenuModule,
    MatTreeModule,
    MatToolbarModule,
  ],
  templateUrl: './nav-bar.component.html',
  styleUrl: './nav-bar.component.css',
})
export class NavBarComponent {
  constructor(private router: Router) {}

  logout() {
    console.log('Cerrando sesión...');
    this.router.navigate(['/']);
  }
}
