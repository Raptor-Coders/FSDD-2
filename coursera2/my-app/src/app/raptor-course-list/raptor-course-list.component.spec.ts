import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RaptorCourseListComponent } from './raptor-course-list.component';

describe('RaptorCourseListComponent', () => {
  let component: RaptorCourseListComponent;
  let fixture: ComponentFixture<RaptorCourseListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [RaptorCourseListComponent]
    });
    fixture = TestBed.createComponent(RaptorCourseListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
