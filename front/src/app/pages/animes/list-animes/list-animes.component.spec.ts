import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListAnimesComponent } from './list-animes.component';

describe('ListAnimesComponent', () => {
  let component: ListAnimesComponent;
  let fixture: ComponentFixture<ListAnimesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListAnimesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListAnimesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
