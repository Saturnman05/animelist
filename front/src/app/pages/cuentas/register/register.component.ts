import { Component, inject } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router, RouterModule } from '@angular/router';

import { AuthService } from '../../../services/auth/auth.service';
import { passwordsMatchValidator } from '../../../utils/form-validator';
import { RegisterRequest } from '../../../models/register.model';

@Component({
  selector: 'app-register',
  imports: [
    MatButtonModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatProgressSpinnerModule,
    ReactiveFormsModule,
    RouterModule,
  ],
  templateUrl: './register.component.html',
  styleUrl: './register.component.scss',
})
export class RegisterComponent {
  registerForm!: FormGroup;
  isLoading = false;
  errorMessage = '';

  private fb = inject(FormBuilder);
  private authService = inject(AuthService);
  private router = inject(Router);
  private _snackBar = inject(MatSnackBar);

  openSnackBar(message: string, action: string): void {
    this._snackBar.open(message, action);
  }

  ngOnInit(): void {
    if (this.authService.isLoggedIn()) {
      this.router.navigate(['/profile']);
      return;
    }

    this.initForm();
  }

  private initForm(): void {
    this.registerForm = this.fb.group(
      {
        username: ['', Validators.required],
        email: ['', Validators.required],
        password: ['', [Validators.required, Validators.minLength(6)]],
        confirmPassword: ['', [Validators.required, Validators.minLength(6)]],
      },
      { validators: passwordsMatchValidator() }
    );
  }

  onRegister(): void {
    if (
      this.registerForm.hasError('passwordsMismatch') &&
      this.registerForm.get('confirmPassword')?.touched
    ) {
      this.openSnackBar('Las contraseñas deben ser iguales.', 'cancelar');
      return;
    }

    if (this.registerForm.invalid) {
      this.openSnackBar('Debes llenar los campos obligatorios.', 'cancelar');
      return;
    }

    this.isLoading = true;
    this.errorMessage = '';

    const registerRequest: RegisterRequest = this.registerForm.value;

    this.authService.register(registerRequest).subscribe({
      next: () => {
        this.isLoading = false;
        this.router.navigate(['/login']);
      },
      error: (err) => {
        console.error(err);
        this.isLoading = false;
        this.errorMessage =
          err.error?.detail || 'Register failed. Please try again.';
        this.openSnackBar(this.errorMessage, 'cancel');
      },
    });
  }
}
