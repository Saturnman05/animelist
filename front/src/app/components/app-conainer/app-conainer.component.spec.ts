import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AppConainerComponent } from './app-conainer.component';

describe('AppConainerComponent', () => {
  let component: AppConainerComponent;
  let fixture: ComponentFixture<AppConainerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AppConainerComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AppConainerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
