const THREE = require('three');
const { FBXLoader } = require('three-stdlib');

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const loader = new FBXLoader();
loader.load('./minion/Minion_FBX.fbx', function (object) {
  scene.add(object);
});

camera.position.z = 5;

function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}
animate();