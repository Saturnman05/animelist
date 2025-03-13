import { Component, inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatTreeModule } from '@angular/material/tree';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatMenuModule } from '@angular/material/menu';
import { Router, RouterModule } from '@angular/router';

import { AuthService } from '../../services/auth/auth.service';

@Component({
  selector: 'app-nav-bar',
  imports: [
    MatButtonModule,
    MatIconModule,
    MatMenuModule,
    MatTreeModule,
    MatToolbarModule,
    RouterModule,
  ],
  templateUrl: './nav-bar.component.html',
  styleUrl: './nav-bar.component.css',
})
export class NavBarComponent {
  private authService = inject(AuthService);
  private router = inject(Router);

  logout() {
    console.log('Cerrando sesión...');
    this.authService.logout();
    this.router.navigate(['/login']);
  }
}
